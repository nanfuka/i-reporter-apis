import re


class Validators:

    def validate_location(self, location):
        """Method where all validations are done"""
        geo_location = re.compile(
            "^[0-9]{2}(.)[0-9]{2}( )[0-9]{2}(.)[0-9]{2}$")

        if not location or location.isspace():
            return 'please enter the location of this redflag'

        elif not geo_location.match(location):
            string1 = 'invalid location, please enter the lat, long cordinates'
            string2 = 'in this formant, 25.22 56.22'
            return string1 + string2

    def validate_input(self, *args):
        """Method where all validations are done"""
        createdby = args[0]
        incident_type = args[1]
        status = args[2]

        if not createdby:
            return 'please enter the id of the creator of this redflag'
        elif not isinstance(createdby, int):
            return 'createdby should be an id of the creator of the redflag'
        elif incident_type == "":
            return 'Enter a redflag.'
        elif incident_type != "redflag" and incident_type != "intervention":
            return 'Incident type should either be a redflag or intervention.'
        elif status != "draft" and status != "resolved" and status != "underinvestigation" and status != "rejected":
            strg1 = "status should either be draft, under"
            strg2 = 'investigation, resolved or rejected'
            return strg1+strg2

    def validate_coment(self, comment):
        """method which validates comment"""
        if comment == "":
            return 'Enter the comment'
        if isinstance(comment, int):
            return 'Comment should be a string'

    def validate_user_details(self, *args):
        """method which validates user_details"""
        firstname = args[0]
        lastname = args[1]
        email = args[2]
        username = args[3]
        password = args[4]
        phoneNumber = args[5]
        isAdmin = args[6]
        othernames = args[7]

        email_validation = re.compile(
            "(^[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-z]+$)")

        if not isinstance(firstname, str) or not isinstance(lastname, str)\
                or not isinstance(username, str) or \
                not isinstance(othernames, str):
            return "Invalid input, Enter a string"
        elif not firstname or firstname == "" or not lastname or\
                lastname == "" or not email or email == "" or \
                not username or username == "" or not password or \
                password == ""or not isAdmin or isAdmin == "":
            return {"message": "Enter only valid data"}
        elif isinstance(phoneNumber, str):
            return "The phone number should be an integer"

        elif isAdmin != 'false' and isAdmin != 'true':
            return "IsAdmin should either be true or false"
        elif not email_validation.match(email):
            return 'Invalid email, it should be in this format; kals@gma.com'

    def validate_options(self, images, videos, data):
        if not images or images == "":
            data['images'] == 'None'
        elif not videos or videos == "":
            data['videos'] == 'None'
