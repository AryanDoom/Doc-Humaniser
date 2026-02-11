chrome.runtime.onMessage.addListener((msg) => {
  if (msg.action === "play") {
    try {
      const log = JSON.parse(msg.data);
      play(log);
    } catch (e) {
      console.error("Invalid JSON log", e);
    }
  }
});

function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

async function focusEditor() {

  const x = window.innerWidth / 2;
  const y = window.innerHeight / 2;

  document.elementFromPoint(x, y)?.dispatchEvent(
    new MouseEvent("mousedown", { bubbles: true })
  );
  document.elementFromPoint(x, y)?.dispatchEvent(
    new MouseEvent("mouseup", { bubbles: true })
  );

  await sleep(500);
}


function sendKey(key) {
  const down = new KeyboardEvent("keydown", { key, bubbles: true });
  const press = new KeyboardEvent("keypress", { key, bubbles: true });
  const up = new KeyboardEvent("keyup", { key, bubbles: true });

  document.activeElement.dispatchEvent(down);
  document.activeElement.dispatchEvent(press);
  document.activeElement.dispatchEvent(up);
}

function backspace() {
  document.activeElement.dispatchEvent(
    new KeyboardEvent("keydown", { key: "Backspace", bubbles: true })
  );
}

async function play(log) {
  if (!location.hostname.includes("docs.google.com")) return;

  console.log("Injected into:", location.href);
  console.log("Starting in 3 seconds… click inside the Doc");

  await sleep(3000);
  await focusEditor();

  for (const item of log) {
    if (item.action === "type") {
      sendKey(item.char);
    } 
    else if (item.action === "backspace") {
      backspace();
    } 
    else if (item.action === "wait") {
      await sleep(item.delay);
      continue;
    }

    await sleep(item.delay || 60);
  }

  console.log("Typing complete.");
}
