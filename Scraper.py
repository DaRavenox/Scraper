import java.net.*;
import java.util.Scanner;
import java.util.regex.Pattern;
import java.io.*;

public class Makerofmakes {

    /**
     * Scrapes twitter
     * @throws Exception 
     */
    public static void main(String[] args) throws Exception {

        Scanner sc = new Scanner(System.in);
        String person = sc.next();

        String read;
        URL site = new URL("https://twitter.com/"+person);
        BufferedReader in = new BufferedReader(new InputStreamReader(site.openStream()));
        System.out.println(person+"'s twitter");
        while((read = in.readLine()) != null){
            if (Pattern.matches("<strong class=\"fullname.*", read.trim())){
                System.out.print("OA: " +format(read) + "-> ");
            }
            
            if(Pattern.matches("<p class=\"TweetTextSize TweetTextSize--.*", read.trim())){
                System.out.println(format(read));}
        }
        in.close();
    }
    



    public static String format(String a){

        a = a.trim();
        a = a.replaceAll("strong class=\"fullname js-action-profile-name show-popup-with-id\"", "");
        a = a.replaceAll("<p class=\"TweetTextSize TweetTextSize--[0-90-9]+px js-tweet-text tweet-text\" lang=\"[a-z]*\" data-aria-label-part=\"[0-9]*\">", "");
        a = a.replaceAll("data-aria-label-part", "");
        String[] list = a.split("[<>]");
        StringBuilder builder = new StringBuilder();
        for(int i = 0; i<list.length; i++){

            if(list[i].matches("^b")){

                builder.append("@"+list[i+1]);
                //System.out.print("@"+list[i+1]+" ");
                i = i+2;
            }
            
            
            else if (list[i].matches("a href.*") || list[i].length() <2|| list[i].matches("/[a-z]+") || list[i].matches("span class.*")){
                
            }
            else{
                builder.append(list[i] = list[i]+" ");
                //System.out.print(list[i]+" ");
            }

        }
        
        a = builder.toString();
        a = a.replaceAll("&amp;", "&");
        a = a.replaceAll("&nbsp;", "");
        a = a.replaceAll("&#39;", "'");
        a = a.replaceAll("&quot;", "\"");
        if(a.length() == 0){
            return "RETWEET";
        }
        return a;
    }


}

