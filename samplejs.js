import java.sql.*;
import java.util.Scanner;

public class VulnerableLogin {

    public static void main(String[] args) throws Exception {

        Connection conn = DriverManager.getConnection(
                "jdbc:sqlite:test.db"
        );

        Scanner scanner = new Scanner(System.in);

        System.out.print("Username: ");
        String username = scanner.nextLine();

        System.out.print("Password: ");
        String password = scanner.nextLine();

        // ❌ VULNERABLE QUERY
        String query =
                "SELECT * FROM users WHERE username = '"
                + username
                + "' AND password = '"
                + password
                + "'";

        Statement stmt = conn.createStatement();

        ResultSet rs = stmt.executeQuery(query);

        if (rs.next()) {
            System.out.println("Login successful");
        } else {
            System.out.println("Invalid credentials");
        }

        rs.close();
        stmt.close();
        conn.close();
    }
}