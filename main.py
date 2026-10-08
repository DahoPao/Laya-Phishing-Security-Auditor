from laya import Router

router = Router()

email= { 
    "subject": "IMPORANT ACCOUNT COMPROMISED",
    "body": "Your paypal account has been compromized. Please click this link to secure it." 
}
questions = {
    "department": {
        "type": "choice",
        "instructions": "What type of email is it realted to.",
        "criteria": {
            "billing": "payments, invoices, refunds, anything financial",
            "account": "accounts, passwords, logins, account access",
            "technical": "technical problems, bugs, or system issues ",
            "questions": "general questions about hospital or patients in the hospital",
            "family-or-friends": "email from family or friends asking about how they are doing, what are they doing, and other general questions that they would ask"
        }
    },
    
    "phishing": {
        "type": "noul",
        "instructions": "Is this email phishing"
    }   
}

result = router.predict(email,questions)

print(result)