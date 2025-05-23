import re


def structured_output(text):
    pattern = r'(\d+)\.\s+(.*?)(?=\s[aA]\))((?:\s[a-d]\)\s.*?)+?)\s+Answer:\s*([a-d]\)\s.*?)(?=\s\d+\.|\Z)'
    matches = re.findall(pattern, text, re.DOTALL)

    for number, question, options_block, answer in matches:
        print(f"{number}.\n{question.strip()}")

        # Extract and clean options
        options = re.findall(r'([a-d]\)\s.*?)(?=\s[a-d]\)|$)', options_block.strip())
        for opt in options:
            print(opt.strip())
        
        print(f"Answer: {answer.strip()}\n")



text = """1. What type of Amazon Machine Image (AMI) is selected for creating a Windows instance? a) Linux AMI b) Windows AMI c) macOS AMI d) Chrome OS AMI Answer: b) Windows AMI 2. What is the default storage selection when creating an EC2 instance? a) Paid tier storage b) Free tier storage (if eligible) c) Custom storage d) No storage Answer: b) Free tier storage (if eligible) 3. What is the default instance type selected when creating an EC2 instance? a) t2.small b) t2.micro c) t2.large d) t2.xlarge Answer: b) t2.micro 4. What is the purpose of creating a key pair when launching an EC2 instance? a) To enable billing b) To secure access to the instance c) To select a storage option d) To choose an instance type Answer: b) To secure access to the instance 5. What are some common use cases for EC2 instances? a) Hosting websites and applications b) Processing large amounts of data c) Performing demanding computing tasks d) All of the above Answer: d) All of the above 6. What is the maximum amount of EBS storage available for free tier eligible users? a) 10 GB b) 30 GB c) 50 GB d) 100 GB Answer: b) 30 GB 7. What is the final step in launching an EC2 instance? a) Creating a key pair b) Selecting a storage option c) Choosing an instance type d) Clicking on "Launch instance" Answer: d) Clicking on "Launch instance" 8. What are the common EC2 instance states in AWS? a) Pending, Running, Stopping b) Pending, Running, Stopping, Stopped, Terminated, Shutting Down, Rebooted c) Running, Stopping, Stopped d) Pending, Stopped, Terminated Answer: b) Pending, Running, Stopping, Stopped, Terminated, Shutting Down, Rebooted 9. Where can you view the state of your EC2 instances? a) EC2 Console b) AWS CLI c) AWS SDKs d) All of the above Answer: d) All of the above 10. Why is it important to keep track of the state of your EC2 instances? a) To manage them properly b) To save costs c) To improve performance d) To increase security Answer: a) To manage them properly
"""
structured_output(text)
