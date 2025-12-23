import os
import time
from dotenv import load_dotenv
from groq import Groq
import colorama
from pathlib import Path 
from colorama import Fore, Style

colorama.init(autoreset=True)

def print_intro():
    print(Fore.GREEN + """
    ██████╗ ██████╗  ██████╗  ██████╗
    ██╔══██╗██╔══██╗██╔═══██╗██╔═══██╗
    ██████╔╝██████╔╝██║   ██║██║   ██║
    ██╔═══╝ ██╔══██╗██║   ██║██║   ██║
    ██║     ██║  ██║╚██████╔╝╚██████╔╝
    ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝
    INTERACTIVE TERMINAL v1.0
    Initializing AI interface...
    """)
    time.sleep(1)
    print(Fore.GREEN + "Loading neural networks...")
    time.sleep(0.5)
    print(Fore.GREEN + "Connecting to quantum servers...")
    time.sleep(0.5)
    print(Fore.GREEN + "Access granted. Welcome, hacker.")
    time.sleep(1)

def type_text(text, color=Fore.GREEN, delay=0.03):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    load_dotenv()
    api_key = os.getenv('GROQ_API_KEY')
    print(Fore.YELLOW + f"Debug: API key loaded - Length: {len(api_key) if api_key else 0}, Starts with: {api_key[:4] if api_key else 'None'}")
    if not api_key:
        print(Fore.RED + f"Error: Could not find GROQ_API_KEY. Checked path: {env_path}")
        return
    client = Groq(api_key=api_key)
    print_intro()
    messages = []
    while True:
        try:
            user_input = input(Fore.WHITE + "Ur@terminal:~$ ")
            if user_input.lower() in ['quit', 'exit', 'q']:
                type_text("Shutting down AI interface...", Fore.RED)
                break
            messages.append({"role": "user", "content": user_input})
            type_text("Processing query...", Fore.YELLOW, delay=0.01)
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=messages,
                max_tokens=1000,
                temperature=0.7
            )
            ai_response = response.choices[0].message.content
            type_text(ai_response, Fore.GREEN)
            messages.append({"role": "assistant", "content": ai_response})
        except KeyboardInterrupt:
            type_text("\nOperation aborted by user.", Fore.RED)
            break
        except Exception as e:
            type_text(f"Error: {str(e)}", Fore.RED)
if __name__ == "__main__":
    main()
