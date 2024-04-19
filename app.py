import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

// Customer class
class Customer {
    private String name;
    private String address;
    private String contactInfo;

    public Customer(String name, String address, String contactInfo) {
        this.name = name;
        this.address = address;
        this.contactInfo = contactInfo;
    }

    // Getters and setters
    // Additional methods as needed
}

// ServiceRequest class
class ServiceRequest {
    private static int nextId = 1;

    private int requestId;
    private String description;
    private String status;

    public ServiceRequest(String description) {
        this.requestId = nextId++;
        this.description = description;
        this.status = "Pending";
    }

    // Getters and setters
    // Additional methods as needed
}

// Account class
class Account {
    private int accountId;
    private double balance;

    public Account(int accountId, double balance) {
        this.accountId = accountId;
        this.balance = balance;
    }

    // Getters and setters
    // Additional methods as needed
}

// CustomerSupportRepresentative class
class CustomerSupportRepresentative {
    private String name;
    private int employeeId;

    public CustomerSupportRepresentative(String name, int employeeId) {
        this.name = name;
        this.employeeId = employeeId;
    }

    // Getters and setters
    // Additional methods as needed
}

// DataAccessLayer class
class DataAccessLayer {
    private static Map<Integer, Customer> customers = new HashMap<>();
    private static List<ServiceRequest> serviceRequests = new ArrayList<>();
    private static Map<Integer, Account> accounts = new HashMap<>();
    private static List<CustomerSupportRepresentative> supportReps = new ArrayList<>();

    public static void addCustomer(Customer customer) {
        customers.put(customers.size() + 1, customer);
    }

    public static void submitServiceRequest(ServiceRequest request) {
        serviceRequests.add(request);
    }

    public static void addAccount(Account account) {
        accounts.put(accounts.size() + 1, account);
    }

    public static void addSupportRep(CustomerSupportRepresentative rep) {
        supportReps.add(rep);
    }

    // Methods to fetch data from database
}

// BusinessLogicLayer class
class BusinessLogicLayer {
    public static void submitServiceRequest(String description) {
        ServiceRequest request = new ServiceRequest(description);
        DataAccessLayer.submitServiceRequest(request);
        System.out.println("Service request submitted successfully.");
    }

    // Additional methods for business logic
}

// CustomerInterface class
class CustomerInterface {
    private static Scanner scanner = new Scanner(System.in);

    public static void submitServiceRequest() {
        System.out.print("Enter description of the issue: ");
        String description = scanner.nextLine();
        BusinessLogicLayer.submitServiceRequest(description);
    }

    // Additional methods for customer interaction
}

// CustomerSupportInterface class
class CustomerSupportInterface {
    // Methods for customer support interaction
}

// Main class to run the application
public class GasUtilityApp {
    public static void main(String[] args) {
        // Application initialization and startup

        // Sample usage: Submit service request as a customer
        CustomerInterface.submitServiceRequest();
    }
}
