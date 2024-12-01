import requests
import datetime
from send_msg import send_message

def makeRequest(url):
    """Make a GET request to API, return response."""
    # make a GET request to api
    return requests.get(url)

def get_ordinal_suffix(day): 
    """Return the correct ordinal suffix for a given day."""
    if 11 <= day <= 13: 
        return "th"
    else: 
        # obtain the last digit in the int
        last_digit = day % 10
        if last_digit == 1: 
            return "st"
        elif last_digit == 2: 
            return "nd"
        elif last_digit == 3: 
            return "rd"
        else: 
            return "th"

def getDate():
    """Return the formatted date."""
    # get and format publish date (will be current date since api does not serve old information)
    d = datetime.datetime.now()
    weekday, day, month, year = d.strftime("%A"), d.day, d.strftime("%B"), d.year

    # return formatted date
    return f"{weekday}, {month} {day}{get_ordinal_suffix(day)}, {year}"

def generateEmail(articles, user_name, message):
    """Return an NBA-styled HTML email."""
    # nba-styled html content
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge"> <!-- render the page using edge mode for IE -->
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <title>NBA Newsletter</title>
        </head>
        <body style="font-family: Arial, sans-serif; background-color: #f0f0f0; padding: 20px;">
            <!-- outer container -->
            <div style="max-width: 600px; margin: 0 auto; background-color: #ffffff; padding: 20px; 
                        border: 2px solid #C9082A; border-radius: 10px; box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);">
                
                <!-- header banner with gradient and centered logo -->
                <div style="background: linear-gradient(90deg, #1E90FF 0%, #C8102E 100%); padding: 20px 0; text-align: center; border-radius: 10px 10px 0 0;">
                    <img src="https://www.logodesignlove.com/images/classic/nba-logo.jpg" alt="nba logo" width="120px" style="margin-bottom: 5px;">
                </div>

                <!-- date below banner, smaller font -->
                <div style="text-align: center; color: #555; font-size: 14px; margin-top: 10px;">
                    {getDate()}
                </div>

                <!-- greeting and headline -->
                <h2 style='color: black; text-align: center; font-size: 22px; margin-top: 10px;'>{message}</h2>
                <hr style="border: 1px solid #C9082A;">
                <ul style='font-family: Arial, sans-serif; list-style-type: none; padding: 0;'>
    """
    
    # alternating colors for articles
    color1 = "#F5F5F5"  # light grey
    color2 = "#FFFFFF"  # white
    toggle = True

    for article in articles:
        headline = article.get("headline", "no headline")
        description = article.get("description", "no description")
        link = article.get("links", {}).get("web", {}).get("href", "#")
        
        # toggle the background color for alternating articles
        background_color = color1 if toggle else color2
        toggle = not toggle # change on each iteration
        
        # append each article's formatted html with alternating background colors
        html_content += f"""
          <li style="background-color: {background_color}; padding: 15px; margin-bottom: 10px; border-radius: 5px; justify-content: space-between; align-items: center;">
                <div style="flex: 1;">
                    <h3 style='font-size: 18px; color: #1D428A; font-weight: bold;'>{headline}</h3>
                    <p style="font-size: 16px; color: #333;">{description}</p>
                </div>
                <a href="{link}" style="background-color: #006BB6; color: white; padding: 10px 15px; text-decoration: none; 
                        border-radius: 5px; display: inline-block; margin-left: 465px; white-space: nowrap;">
                    Learn More
                </a>
            </li>
        """
    
    # close the html structure
    html_content += """
                </ul>
                <hr style="border: 1px solid #C9082A;">

                <!-- footer section with social media links -->
                <div style="text-align: center; margin-top: 20px;">
                    <p style="color: #777; font-size: 12px;">Stay connected:</p>
                    <a href="https://www.twitter.com/nba" target="_blank" style="margin-right: 10px;">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/b/b7/X_logo.jpg" alt="X" width="20px">
                    </a>
                    <a href="https://www.facebook.com/nba" target="_blank" style="margin-right: 10px;">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/2023_Facebook_icon.svg/600px-2023_Facebook_icon.svg.png?20231011122028" alt="Facebook" width="20px">
                    </a>
                    <a href="https://www.instagram.com/nba" target="_blank">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" alt="Instagram" width="20px">
                    </a>
                </div>

                <!-- copyright notice -->
                <div style="text-align: center; font-size: 12px; color: #777; margin-top: 20px;">
                    <p>&copy; NBA 2024 | All Rights Reserved</p>
                </div>
            </div>
        </body>
    </html>
    """

    return html_content

# due to a change in the resource, this is no longer usable
def checkDates(fetched_date): 
    """Check the fetched and current date. Return T/F after checking for a match."""
    # obtain the current date in the correct format
    current_date = str(datetime.datetime.now()).split()[0]

    # check to see if the fetched date is the same as the current date
    # a fail here means there is no new data
    return (current_date == fetched_date)

def main(): 
    # provide url to API endpoint
    url = "https://site.api.espn.com/apis/site/v2/sports/basketball/nba/news"

    # create the list of recipients *** (this should be changed)
    RECIPIENTS = {
    }

    # call function
    response = makeRequest(url) 

    if response.status_code == 200: # if successful
        # obtain the json object
        data = response.json()

        # access list of articles
        articles = data.get("articles", [])        
        
        # iterate through the list of recipients
        for user_name, user_email in RECIPIENTS.items():
            # generate HTML email content
            html_email = generateEmail(articles, user_name, f"Hi {user_name}, here's today's NBA news")
            # use imported function to send the email
            send_message(user_email, html_email, f"Today's NBA news ({getDate()})")

    else: 
        print(f"Failed to retrieve data: {response.status_code}")

main()