import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.net.URI;

public class ApiClient {
    public static void main(String[] args) throws Exception {
        // create HTTP client
        HttpClient client = HttpClient.newHttpClient();

        // build request to your Django API
        HttpRequest request = HttpRequest.newBuilder()
            .uri(URI.create("http://127.0.0.1:8000/api/entries/"))
            .GET()
            .build();

        // send request and get response
        HttpResponse<String> response = client.send(
            request, HttpResponse.BodyHandlers.ofString()
        );

        System.out.println("Status: " + response.statusCode());
        System.out.println("Data from Django API:");
        System.out.println(response.body());
    }
}