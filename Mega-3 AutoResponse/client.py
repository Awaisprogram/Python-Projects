import google.generativeai as genai
import time

# Configure API key
genai.configure(api_key="")  # Replace with a valid key

def aiProcess(command):
    try:
        print("\nChatbot: (Thinking... ⏳)")  # Show loading message
        time.sleep(1)  # Simulating processing delay

        model = genai.GenerativeModel("gemini-1.5-pro")
        response = model.generate_content(command, generation_config={
            "max_output_tokens": 20,
            "temperature": 0.7,
        })
        
        return response.text if response else "I'm sorry, I couldn't process that."
    
    except Exception as e:
        if "429" in str(e):
            return "Error: Too many requests! 😵 Please wait or check your quota."
        return f"Error: {e}"

# Continuous input loop
while True:
    print("\nAsk anything\n")
    command = input("You: ")
    
    if command.lower() == "exit":
        print("\nGoodbye! 👋")
        break
    
    response = aiProcess(command)
    print(f"\nChatbot: {response}")
    time.sleep(0.5) 
