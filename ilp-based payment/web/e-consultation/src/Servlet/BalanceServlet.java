package doctor;

import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet(urlPatterns={"/Balance"}, name = "Balance")
public class BalanceServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpClient client = HttpClients.createDefault();
        String user = request.getParameter("user");
        HttpGet get = new HttpGet("http://127.0.0.1:7770/accounts/" + user + "/balance");
        String token = request.getParameter("token");
        get.setHeader("Authorization", "Bearer " + token);
        HttpResponse response1 = client.execute(get);
        response.getWriter().println(EntityUtils.toString(response1.getEntity()));
    }
}
