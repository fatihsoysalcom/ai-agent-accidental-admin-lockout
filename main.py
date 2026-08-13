import os

CONFIG_FILE = "security_policy.conf"

def create_initial_config():
    """Creates a dummy configuration file with some 'insecure' defaults."""
    content = """
# Simulated Security Policy Configuration
[access]
default_admin_access = true  # This is needed for initial setup/recovery
guest_access = true          # Agent might target this
api_key_visibility = internal_only
debug_mode = false

[network]
allow_all_traffic = false
"""
    with open(CONFIG_FILE, "w") as f:
        f.write(content.strip())
    print(f"--- Initial '{CONFIG_FILE}' content ---")
    print(content.strip())
    print("-" * 40)

def simulate_ai_agent_action():
    """
    Simulates an AI agent attempting to 'harden' security configurations.
    This demonstrates an unintended consequence (accidental lockout).
    """
    print("AI Agent: Task received - 'Harden security configurations by removing overly permissive defaults.'")
    print("AI Agent: Analyzing configuration file...")

    lines = []
    with open(CONFIG_FILE, "r") as f:
        lines = f.readlines()

    modified_lines = []
    has_unintended_consequence = False
    for i, line in enumerate(lines):
        new_line = line

        # AI Agent's autonomous logic: Identify common insecure defaults and try to disable them.
        # This is where the 'autonomy' and lack of full context can lead to issues.
        if "default_admin_access = true" in line.lower():
            # This line is critical for initial admin access or recovery.
            # The agent, without full context of the system's operational requirements,
            # might interpret "default" and "true" as inherently insecure.
            new_line = line.replace("true", "false") # Agent changes it to 'false'
            has_unintended_consequence = True
            print(f"AI Agent: Modified '{line.strip()}' -> '{new_line.strip()}' (Intended: disable default access)")
            # This modification, while seemingly logical for hardening, accidentally disables
            # critical administrative access, leading to an 'accidental hack' (denial of access).
        elif "guest_access = true" in line.lower():
            # This is a more benign change, likely intended and safe.
            new_line = line.replace("true", "false")
            print(f"AI Agent: Modified '{line.strip()}' -> '{new_line.strip()}' (Intended: disable guest access)")
        
        modified_lines.append(new_line)

    with open(CONFIG_FILE, "w") as f:
        f.writelines(modified_lines)

    print("\nAI Agent: Configuration hardening complete.")
    if has_unintended_consequence:
        print("--- WARNING: Potential Unintended Consequence ---")
        print("The AI agent, in its attempt to harden security, may have accidentally disabled")
        print("critical 'default_admin_access'. This could lead to an administrative lockout,")
        print("demonstrating how autonomous agents can cause 'accidental hacks' without malicious intent.")
    print("-" * 40)

def display_final_config():
    """Displays the final content of the configuration file."""
    print(f"\n--- Final '{CONFIG_FILE}' content after AI Agent action ---")
    with open(CONFIG_FILE, "r") as f:
        print(f.read().strip())
    print("-" * 40)

def cleanup():
    """Removes the created configuration file."""
    if os.path.exists(CONFIG_FILE):
        os.remove(CONFIG_FILE)
        print(f"\nCleaned up: '{CONFIG_FILE}' removed.")

if __name__ == "__main__":
    try:
        create_initial_config()
        simulate_ai_agent_action()
        display_final_config()
    finally:
        cleanup()
