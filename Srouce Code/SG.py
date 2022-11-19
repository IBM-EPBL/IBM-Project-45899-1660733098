from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(from_email='james.m.cse.2019@snsct.org',
    to_emails='jamessandal@gmail.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>Project Name :: Smart Fashion Recommender Application</strong><br><strong>Tokyo the SengGrid Bot here!</strong>')
try:
    sg = SendGridAPIClient('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')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)