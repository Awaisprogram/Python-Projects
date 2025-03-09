import pyautogui
import time
import pyperclip
import google.generativeai as genai



# Configure API key
genai.configure(api_key="")  # Replace with a valid key


pyautogui.click(1019 , 787)
time.sleep(1)

pyautogui.moveTo(790,  114)
pyautogui.dragTo(1179  ,250, duration=1.0 , button="left" )


pyautogui.hotkey('command', 'c')
pyautogui.click(597 ,91)

time.sleep(1)  # Allow clipboard time to update

chat_history = pyperclip.paste()

print(chat_history)

def aiProcess(chat_history):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro")  
        response = model.generate_content(chat_history, generation_config={
            "max_output_tokens": 20,
            "temperature": 0.7,
        })
        return response.text if response and hasattr(response, 'text') else "Error: No response received."
    except Exception as e:
        return f"Error: {e}"
    
ai_response = aiProcess(chat_history)
print("AI Response:", ai_response)