package doctor;

import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet(urlPatterns={"/Pay"}, name = "PayServlet")
public class PayServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpClient client = HttpClients.createDefault();
        String user = request.getParameter("user");
        HttpPost post = new HttpPost("http://127.0.0.1:7770/accounts/" + user + "/payments");
        String token = request.getParameter("token");
        post.setHeader("Authorization", "Bearer "+token);
        post.setHeader("content-type", "application/json");
        String receiver = request.getParameter("receiver");
        String amount = request.getParameter("amount");
        String reqStr = "{\"receiver\": \"" + receiver + "\",\"source_amount\": " + amount + "}";
        System.out.println(reqStr);
        StringEntity entity = new StringEntity(reqStr, "utf-8");
        post.setEntity(entity);
        HttpResponse response1 = client.execute(post);
        response.getWriter().println(EntityUtils.toString(response1.getEntity()));
        response.setStatus(response1.getStatusLine().getStatusCode());

    }
}
