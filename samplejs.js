// VulnerableApp.java
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class VulnerableApp {
    public static void main(String[] args) throws Exception {
        BufferedReader reader =
                new BufferedReader(new InputStreamReader(System.in));

        System.out.print("Enter host: ");
        String host = reader.readLine();

        // VULNERABLE: Command Injection
        Process process = Runtime.getRuntime().exec("ping " + host);

        BufferedReader output =
                new BufferedReader(
                        new InputStreamReader(process.getInputStream()));

        String line;

        while ((line = output.readLine()) != null) {
            System.out.println(line);
        }
    }
}