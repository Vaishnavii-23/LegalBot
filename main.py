# main.py

from dotenv import load_dotenv
from crew import legal_assistant_crew

load_dotenv()

def run(user_input: str):
    result = legal_assistant_crew.kickoff(inputs={"user_input": user_input})

    print("-"*50)
    print(result)
    print("-" * 50)

if __name__ == "__main__":
    user_input = (
        "A man broke into my house at night while my family was sleeping. "
        "He stole jewelry and cash from our bedroom. When I confronted him, "
        "he threatened me with a knife and ran away. We reported it to the police, "
        "but I'm not sure which legal charges should be filed under IPC."
    )

    run(user_input)
