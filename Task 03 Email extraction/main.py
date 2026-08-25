import re
import os

email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

def read_file(filename):
    """Read the entire content of a text file. Returns the text or None on failure."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        print(f"File '{filename}' not found. Make sure it's in the same folder as this script.")
        return None
    except IOError as e:
        print(f"Could not read file: {e}")
        return None


def extract_emails(text):
    """Find all email addresses in the given text using regex."""
    emails = re.findall(email_pattern, text)
    unique_emails = sorted(set(emails))         
    return unique_emails


def save_emails(emails, output_filename="extracted_emails.txt"):
    """Write the extracted emails to a new text file, one per line."""
    try:
        with open(output_filename, "w", encoding="utf-8") as file:
            for email in emails:
                file.write(email + "\n")
        print(f"{len(emails)} email(s) saved to '{output_filename}'")
    except IOError as e:
        print(f"Could not save file: {e}")


def main():
    print("=" * 40)
    print("   EMAIL EXTRACTOR")
    print("=" * 40)

    input_filename = input("Enter the .txt filename to scan (e.g. data.txt): ").strip()

    text = read_file(input_filename)
    if text is None:
        return

    emails = extract_emails(text)

    if not emails:
        print("\nNo email addresses found in the file.")
        return

    print(f"\nFound {len(emails)} unique email(s):")
    for email in emails:
        print(f"  - {email}")

    save_emails(emails)


if __name__ == "__main__":
    main()