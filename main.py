from predict import predict_email

def run_interactive_detector():
    """
    Runs and interactive command line for the phishing detector
    """
    print("========================================")
    print("   AI Phishing Email Detector")
    print("========================================")
    print("Paste the content of an email below.")
    print("Type 'exit' or 'quit' on a new line to end the program.\n")

    while True:
        # Get multi-line input from the user
        print("Enter email text (press Ctrl+D on a new line when done, or Ctrl+Z on Windows):")
        
        lines = []
        try:
            while True:
                line = input()
                lines.append(line)
        except EOFError:
            pass # This is how we detect the end of input

        user_input = "\n".join(lines)

        # Check if the user wants to quit
        if user_input.lower().strip() in ['exit', 'quit']:
            print("Exiting detector. Goodbye!")
            break
        
        # If input is empty, prompt again
        if not user_input.strip():
            print("\nNo input received. Please paste email text.\n")
            continue

        # Make a prediction
        result = predict_email(user_input)
        
        # Print the result in a clean format
        print("\n" + "="*20)
        print("Analysis Result:")
        print(f"  {result}")
        print("="*20 + "\n")


if __name__ == '__main__':
    # Important Note: This will only work AFTER you have run train.py
    # and the model files exist in the /models directory.
    run_interactive_detector()