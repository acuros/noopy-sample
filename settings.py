PROJECT_NAME = 'sample'
ACCOUNT_ID = 'ACCOUNT_ID'  # Your AWS account id
LAMBDA = {
        'Prefix': 'Sample',  # Prefix for lambda function name
        'Role': 'arn:aws:iam::ACCOUNT_ID:role/ROLE_NAME',  # Role arn to be granted to lambda function
}
ENDPOINTS = [  # python files use noopy.endpoint.decorators.endpoint
        'views'
]
