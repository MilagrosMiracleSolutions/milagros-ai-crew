from flask import Flask, request
from flask_mail import Mail, Message

app = Flask(__name__)

# === UPDATE THESE ===
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'milagrosmiraclesolutions@gmail.com'
app.config['MAIL_PASSWORD'] = 'tbhpnwjvehawgkmc'   # ← Replace with your real App Password
app.config['MAIL_DEFAULT_SENDER'] = ('Milagros Miracle Solutions', 'info@milagrosmiraclesolutions.com')

mail = Mail(app)

@app.route('/webhook', methods=['POST'])
def handle_lead():
    name = request.form.get('your-name', 'Client')
    email = request.form.get('your-email')
    phone = request.form.get('your-phone', 'No phone')
    message = request.form.get('your-message', '')

    print(f"New lead from {name} ({email})")

    proposed_reply = f"""Hi {name},

Thank you for reaching out to Milagros Miracle Solutions!

I'd love to help with your cleaning needs — especially "{message}".

When are you available this week for a quick chat or to schedule your deep clean?

Looking forward to making your home sparkle!

Best regards,
Milagros Miracle Solutions
(617) 792-6745"""

    # Send approval request to YOU
    approval = Message(
        subject=f"🔔 New Lead Approval Needed - {name}",
        recipients=["rfelipe95@gmail.com"],
        body=f"""New lead received!

Name: {name}
Email: {email}
Phone: {phone}
Message: {message}

=== PROPOSED REPLY TO SEND ===
{proposed_reply}

Reply to this email with "APPROVE" (or any changes you want) and I'll send it right away."""
    )
    mail.send(approval)

    print("✅ Approval request sent to you.")
    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080) 
