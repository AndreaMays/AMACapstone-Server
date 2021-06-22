# AMA Server Side App

## Prerequisites

### Mac OS

```sh
brew install libtiff libjpeg webp little-cms2
```

### Linux (WSL)

```sh
sudo apt-get install libtiff5-dev libjpeg8-dev libopenjp2-7-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk \
    libharfbuzz-dev libfribidi-dev libxcb1-dev
```

### Install 
<!-- Run the following command to install pipenv -->
```
pip3 install --user pipx
pipx install pipenv

```

## Setup

1. Clone this repository and change to the directory in the terminal.
1. Run `pipenv shell`
1. Run `pipenv install`


Now that your database is set up all you have to do is run the command:

```sh
python manage.py runserver
```

## Bangazon ERD

Open the [AMA Database Diagram ](https://lucid.app/lucidchart/36e31f7c-cf57-4569-a6f0-8df144221735/edit?beaconFlowId=E1E6C23275C9ADCA&invitationId=inv_809734b3-9a7d-42ca-ab49-75b871e20a12&page=UBPJnQTHcbYK#) in the browser to view the tables and relationships for the app's database.

## Postman Request Collection

1. Open Postman
1. Choose the Link option
1. Paste in this URL: (example below)
    `http://localhost:8000/competitionlists`

To test it out, under "Headers", in the "Key" field type in "Authorization". In the value put in the following token```Token 43d31da5331da4b434cb2ccce159fcc49ece1324``` and press "Send". You should get a response back that looks like this.

```json
{

        "date": "2020-11-28",
        "name_of_comp": "Guild",
        "score": "Pass",
        "award": 1,
        "student_user": {
            "user": {
                "first_name": "Kaleb",
                "last_name": "Boone",
                "email": "",
                "id": 4
  
}
```

## Documentation to view client side/full app

To view browser-based documentation for the project, follow these steps.

1. Run `npm start`
1. RSign in as "test@me.com" 
1. Use the password "me" *all lowercase*


![documentation site](./bangazon-docs.png)