# NBA News Messenger

This project sends daily NBA news updates via email by using the ESPN API, and formats them into a neat, NBA-themed email.

## Features

- Retrieves the latest NBA news from the ESPN API.
- Sends a daily email at a scheduled time with a neatly formatted HTML email, including links to articles and descriptions.
- NBA-themed design with the official logo, social media icons, and alternating background colors for each article.
- Automatic scheduling opportunities using Windows Task Scheduler or other schedulers.

## Email Design

Below are screenshots of the email layout:

![NBA News Email - Top](Screenshots/SS%231.png)
![NBA News Email - Bottom](Screenshots/SS%232.png)

## Prerequisites

To run this project, ensure you have the following:

- Python 3 installed on your system.
- Access to your email account's SMTP settings (Gmail recommended).
- An App Password for your Gmail account (if you have 2-step verification enabled). You can learn more about setting up an App Password for Gmail [here](https://support.google.com/accounts/answer/185833).

## Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/nifemi-l/NBA-News-Messenger.git
   ```

2. **Install required libraries**:
   Install the requests module using pip:
   ```bash
   pip install requests
   ```

3. **Update the email sender configuration**:
   Open the `send_msg.py` file and update the following:
   - `EMAIL = "***your-email@gmail.com***"`
   - `PASSWORD = "***your-app-password***"`

4. **Scheduling the script to run automatically**:
   - If you're using **Windows**, you can schedule the script using **Task Scheduler** to run daily at a specific time. 
   - Alternatively, use **cron jobs** for Linux/macOS.

## Running the Project

To run the project manually, use the following command:
```bash
python main.py
```

## Customization

You can customize the following parts of the project:

- **Recipient Email**: Change the recipient email address in the `send_message` function in `send_msg.py`:
  ```python
  send_message('***recipient-email***', html_email, f"NBA News for {getUserName()} - {getDate()}")
  ```
- **User Name**: Change the user name in the `getUserName` function in `main.py`:
  
- **Email Schedule**: Adjust the schedule by changing the timing in **Task Scheduler** (Windows) or using **cron** (Linux/macOS).

## Troubleshooting

- If you don't receive emails, double-check that your email credentials (App Password, email, etc.) are correct.
- Ensure that the email-sending feature works by running the script manually first. 
- For setting up the App Password for Gmail, refer to this [guide](https://support.google.com/accounts/answer/185833).

## License

This project is licensed under the MIT License.
