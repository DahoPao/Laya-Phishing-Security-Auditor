# Laya Phishing Security Auditor

A phishing email security auditor built with [Laya](https://pypi.org/project/laya/).

The project takes an email, asks Laya a set of structured security questions, and returns decisions about the email, including its department and a phishing score.


## Current Features

The current version can:

* Take an email subject and body as input
* Classify the email into a predefined department
* Estimate whether the email is phishing using a yes/no decision (noul)
* Return probabilities for the available departments
* Return structured results that can be processed further in Python

## How It Works

The current workflow is:

```text
Email
  ↓
Python
  ↓
Laya
  ↓
Structured decisions
  ↓
Python processes the results
```

The program asks Laya two questions about each email:

```text
What type of email is it related to?

- billing           (payments, invoices, refunds)
- account           (accounts, passwords, logins)
- technical         (bugs, outages, system errors)
- questions         (general questions)
- family-or-friends (personal email from friends or family)

Is this email phishing?
```

Laya then returns structured information such as:

```text
department:
    account           → 60.33%
    technical         → 19.80%
    family-or-friends → 9.92%
    billing           → 6.33%
    questions         → 3.62%

phishing:
    99.99%
```

This example shows the output from one test email. It is not a benchmark result.

The output is structured data rather than a normal conversational response, which allows Python to access and process individual results.

## Why I Made This

I wanted to learn more about decision-focused AI models and explore how they could be applied to cybersecurity and everyday life.

Rather than building another general-purpose chatbot, I wanted to create something that takes real input, makes structured decisions, and produces results that can be measured and evaluated.

This is also one of my first projects working with AI models through Python, so I built it while learning how the Python code, dictionaries, model inputs, and model outputs fit together.

## Current Status

This project is currently an early prototype.

The immediate goal is to make the basic Laya phishing auditor work reliably before expanding the project into a larger evaluation and benchmarking system.


For example:

```python
result["answers"]["department"]["probabilities"]
```

allows Python to access a specific part of the model's output instead of treating the entire response as one piece of text.

## Notes

The current Laya checkpoint is over-confident out of the box, so the returned values should not be treated as calibrated real-world probabilities.

For this prototype, the phishing (`noul`) value is treated as a model score rather than a guaranteed probability. Calibration and reliability will be evaluated in a later stage of the project.

## Future Plans

Planned improvements include:

* Build a larger dataset of phishing and legitimate emails
* Automatically evaluate many emails
* Add additional security-related questions
* Measure accuracy, precision, recall, and other metrics
* Compare Laya against general-purpose LLMs of different sizes
* Visualize and compare the results

## What I Learned

While building this project, I learned about:

* Python dictionaries and nested dictionaries
* Passing structured data to an AI model
* Reading values from nested dictionaries
* Laya's `choice`, `score`, and `noul` decision types
* Using an AI model from Python
* Processing structured model output programmatically

## Development Process

This project took me roughly a day and a half to build.

I am still early in my programming and AI journey, so I built the project by learning each part as I went. I used AI as a learning assistant to explain concepts, help identify mistakes, and clarify how different parts of the code worked. I wrote and structured the project myself.


The long-term goal is to investigate how a small decision-focused model such as Laya compares with larger general-purpose language models on phishing detection.

## Disclaimer

This project is for learning and experimentation.

It is not intended to be a production phishing detection system and should not be used as the sole method for making real-world security decisions.
