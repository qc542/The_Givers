from database import organizationService

testOrgs = [
    {
        "name": "Red Cross",
        "email": "redcross@gmail.com",
        "location": "Washington, DC",
        "category": "Health",
        "summary": "Red Cross volunteers and staff work to deliver vital services – from providing relief and support to those in crisis, to helping you be prepared to respond in emergencies.",
    },
    {
        "name": "Humane Society",
        "email": "humanesociety@gmail.com",
        "location": "Washington, DC",
        "category": "Animals",
        "summary": "The Humane Society of the United States (HSUS) is an American nonprofit organization that focuses on animal welfare and opposes animal-related cruelties of national scope.",
    },
    {
        "name": "UNICEF",
        "email": "unicef@gmail.com",
        "location": "New York, NY",
        "category": "Humanitarian",
        "summary": "UNICEF, also known as the United Nations Children's Fund,[a] is a United Nations agency responsible for providing humanitarian and developmental aid to children worldwide.",
    },
    {
        "name": "Amnesty International",
        "email": "amnesty@gmail.com",
        "location": "London, UK",
        "category": "Human Rights",
        "summary": "The stated mission of the organization is to campaign for 'a world in which every person enjoys all of the human rights enshrined in the Universal Declaration of Human Rights and other international human rights instruments.'",
    },
    {
        "name": "Food Bank For New York City",
        "email": "donorservices@foodbanknyc.org",
        "location": "New York, DC",
        "category": "Food Insecurity",
        "summary": "Our mission is to end hunger by organizing food, information and support for community survival, empowerment, and dignity.",
    },
]

for org in testOrgs:
    result = organizationService.addOrganization(
        org["name"], org["email"], org["location"], org["category"], org["summary"]
    )
    print(result)
