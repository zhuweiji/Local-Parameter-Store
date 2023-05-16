# Local-Parameter-Store

Local-Parameter-Store is a web-based solution for managing and retrieving parameter values securely. It aims to address the challenges of managing environment variables across different environments, especially when working with remote VMs or in multi-developer projects.

## Key Features

- **Centralized Parameter Storage:** The parameter store provides a centralized location for storing and managing parameter values, eliminating the need to manage environment files across different environments.

- **Secure Parameter Retrieval:** Parameters can be retrieved securely by making authenticated requests to the parameter store's HTTPS endpoint. Requests for parameter values are authenticated by sending a message to a private Telegram Bot chat with the owner of the parameter store. This ensures that only authorized users can retrieve parameter values.


## Getting Started

Follow these steps to set up and use the Local-Parameter-Store:

1. **Installation:** Clone the repository and install the required dependencies. Usage of poetry as the dependency manager is recommended, although installing via pip and requirements.txt is available too.

2. **Configure Telegram Authentication:** Set up the Telegram Bot integration by creating a private chat with the owner of the parameter store and obtaining the necessary authentication details.

3. **Start the Parameter Store:** Run the parameter store webserver, ensuring that it is accessible via the specified HTTPS endpoint.

5. **Retrieve Parameters:** Make authenticated requests to the parameter store's HTTPS endpoint, providing the necessary authentication details and the parameter name to retrieve the corresponding parameter value securely.

<!-- For detailed installation instructions and usage examples, please refer to the [User Guide](user-guide.md). -->

## Contributing

Contributions to the Local-Parameter-Store are welcome! If you encounter any issues, have suggestions for improvements, or would like to contribute new features, please submit a pull request or open an issue in the repository.

