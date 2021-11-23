import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;


import java.io.*;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;

public class Latency {

    public static void main(String[] args) {
        File file = new File("latencies");
        FileWriter fileWriter = null;
        try {
            fileWriter = new FileWriter(file);
        } catch (IOException e) {
            e.printStackTrace();
        }

        for(int i=1;i<=10;i++) {
            int j = 0;
            while(j<10) {
                HttpClient client = HttpClients.createDefault();
                HttpPost post = new HttpPost("http://127.0.0.1:7770/accounts/alice/payments");
                post.setHeader("Authorization", "Bearer alice_password");
                post.setHeader("content-type", "application/json");
                int amount = (int) (i * 10 * 0.0028 * 1000000);
                String reqStr = "{\"receiver\": \"" + "http://charlie-node:7770/accounts/charlie/spsp" + "\",\"source_amount\": " + amount + "}";
                System.out.println(reqStr);
                StringEntity entity = new StringEntity(reqStr, "utf-8");
                post.setEntity(entity);
                HttpResponse response1 = null;
                try {
                    Date start = new Date();
                    response1 = client.execute(post);
                    Date end = new Date();
                    long time = end.getTime() - start.getTime();
                    if (response1.getStatusLine().getStatusCode() == 200) {
                        System.out.println(time);
                        fileWriter.write(i+":"+time+" ");
                        fileWriter.flush();
                        j++;
                    } else{
                        System.out.println(response1.getStatusLine().getStatusCode());
                    }
                    Thread.sleep(2000);
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
            try {
                fileWriter.write("\n");
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}
