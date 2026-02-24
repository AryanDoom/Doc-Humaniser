# Doc Humanizer

Doc Humanizer is an AI powered utility that converts AI-generated text into human-like typing patterns. It consists of a Python backend that generates a realistic keystroke log and a Chrome extension that replays this log directly into Google Docs, simulating natural human typing speed, pauses, and occasional typos.

## Core Features

*   **AI Essay Engine**: Uses Google Gemini to write essays with a natural, "humane" tone.
*   **Typing Simulator**: Generates a JSON log of keystrokes with randomized delays.
*   **Error Simulation**: Automatically inserts and corrects small typos to mimic real human behavior.
*   **Native Integration**: Replays the typing pattern directly into Google Docs via a Chrome extension.

---

## Technical Specifications

*   **Language Model**: Gemini 2.5 Flash
*   **Typing Logic**: Python with randomized delay distributions
*   **Platform**: Google Docs (Chrome/Chromium)

---

## Installation and Setup

### 1. Prerequisites
*   Python 3.x installed.
*   Google Generative AI SDK installed.

### 2. Backend Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/Doc-Humaniser.git
cd Doc-Humaniser

# Install the Python SDK
pip install google-genai
```

### 3. API Configuration
You need a Google AI Studio API key. Set it in your environment:

```bash
# On Windows (PowerShell)
$env:DOOM_BOT_KEY = "your_api_key_here"

# On Windows (Command Prompt)
set DOOM_BOT_KEY=your_api_key_here
```

### 4. Extension Setup
1.  Open Chrome and navigate to `chrome://extensions/`.
2.  Enable **Developer mode**.
3.  Click **Load unpacked**.
4.  Select the project folder containing the `manifest.json`.

---

## How to Use

### Step 1: Generate the Pattern
Run the Python script to generate your essay and its corresponding keystroke log.

```bash
python logic.py
```
This will produce a file named `keystrokes.json`.

### Step 2: Load the Extension
1.  Open the Google Doc where you want the text to appear.
2.  Click the **Doc Humanizer** extension icon in your toolbar.
3.  Open `keystrokes.json` and copy its entire content.
4.  Paste the content into the **Paste Log Data** box in the extension popup.

### Step 3: Start Writing
1.  Click **Start Writing**.
2.  Immediately click inside the Google Doc editor within 3 seconds.
3.  Watch as the AI "types" your essay like a human.

> [!WARNING]  
> Make sure to keep the Google Doc tab active and focused while the extension is running to ensure the typing simulation works correctly.
