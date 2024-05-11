# LootGen

![Logo](https://bitbucket.org/lootgen/lootgen-repository/raw/6ba5802e7f502cf98dd4cb08246c7368a95d9186/static/images/lootgen_logo_only_outline_blackVersion3-p-500.png)

## Description

This program serves as an advanced assistant to Dungeons and Dragons players and Dungeon Masters. With this program, you may run requests to have your characters evaluated by an AI assistant that will provide either suggestions about appropriate Wizards of the Coast created magical loot, or you may request that the AI create new loot for you in line with the magic item creation rules set for in the 5th Edition Dungeon Master's Guide.

## Status

[![CodeQL](https://github.com/s0frl15/LootGen/actions/workflows/codeql.yml/badge.svg)](https://github.com/s0frl15/LootGen/actions/workflows/codeql.yml)
[![Bandit](https://github.com/s0frl15/LootGen/actions/workflows/bandit.yml/badge.svg)](https://github.com/s0frl15/LootGen/actions/workflows/bandit.yml)

## Dependencies, Frameworks and Technologies Used

![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=for-the-badge&logo=tailwind-css&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![AJAX](https://img.shields.io/badge/AJAX-FF6900?style=for-the-badge&logo=ajax&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white)
![ChatGPT](https://img.shields.io/badge/ChatGPT-000000?style=for-the-badge&logo=openai&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3ECF8E?style=for-the-badge&logo=supabase&logoColor=white)
![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black)

## Installation Instructions

### Prerequisites

### Set Up a Virtual Environment

First, create a virtual environment in you project directory. You can do this by running the following command in your terminal:

```bash
> python -m venv venv
```

Activate the virtual environment:

- On Windows, use:

  ```bash
  > venv\Scripts\activate
  ```

- On macOS and Linux, use:

  ```bash
  $ source venv/bin/activate
  ```

### API dependencies

This repository does not come with API keys to the required Firebase Authentication database, the Supabase database, nor the OpenAI assistant.

In the event that the creators of this program would like you to test their work or offer you access to their edition of these dependencies, the API keys will be provided in the zip folder you receive directly.

Should you wish to use this without the authors' API keys, you will be required to set up your own Firebase authentication database, Supabase content database, and OpenAI assistant. The authors of this program may provide support in setting up the databases at their discretion.

### Install Required Libraries

Install all required external libraries by running:

```bash
> pip install flask supabase pyrebase4 firebase firebase-admin==5.0.0 openai==0.28
```

or alternatively you can install with (from the root directory):

```bash
> pip install requirements.txt
```

This command installs the required library dependencies needed to support this application.

### Running the Application

To run the application, use the following command:

```bash
> python LootGen_app.py
```

There will be a slight delay as the health check file ensures all API keys are active. Please wait for confirmation in the terminal.

Once completed, this will start the Flask server, and you should see the application running on `http://localhost:5000`.

Press Ctrl and click where it says `http://localhost:5000` to launch the application in your browser.

## Usage Guide

A complete user manual can be requested by the creators of this application by emailing them at LootGen.ai@gmail.com

## Contributing

If you would like to contribute to this project, please email LootGen.ai@gmail.com with a request to join the project. This is not an open source project and contribution requests will be rejected unless you are explicitly authorized to join the project.

## License

LootGen and its creators provide no license, grantees, warranties, or endorsements for anyone to use this product. This application is solely intended for use by the creators and those they invite to use the application.

## Authors and Acknowledgement

### Team LootGen is comprised of the following members:

Levi Franklin - Project Manager, Backend Engineering Lead, Database Manager

Dylan De La Rosa - UI/UX Design Lead, Frontend Engineer, AI Expert, QA, Process Engineer

Sam Lea - Documentation Lead, Frontend Developer

Collin Trehar - Integrations Manager

### LootGen would like to thank the following for their support:

Dr. Srujan Kotikela - Our computer science professor, mentor, and stakeholder. We could not have done this without your guidance.

Our friends, family, and significant others - Thank you for putting up with the long nights of coding, the hair pulling mental breakdowns, and the general state of panic.

## Project Status and Future Roadmap

The core of LootGen has been completed as required by the initial catalyst for its creations. The ability to create an account, add characters, and request evaluation is complete. However, members of the team have expressed interest in furthering this program in order to support storage of LootGen created items, more detailed charater analysis, and monster encounter recommendations.

## Contact Information

Please reach out to us at LootGen.ai@gmail.com for any inquiries about this project. Project Manager Levi Franklin will respond to you as soon as possible.
