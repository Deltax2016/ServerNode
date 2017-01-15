#include <ESP8266WiFi.h>
#include <WiFiClient.h>
#include <ESP8266WebServer.h>
#include <ESP8266mDNS.h>
#include <ESP8266HTTPClient.h>
#define THERMISTORPIN A0 

const char *ssid = "DeltaX";
const char *password = "88888888";

ESP8266WebServer server ( 80 );
String celsiy="23";
short int qwert = 0;

void handleRoot() {

  char temp[400];
  snprintf ( temp, 400,

"<html>\
  <head>\
    <meta http-equiv='refresh' content='5'/>\
    <title>SmartOK</title>\
    <style>\
      body { background-color: #cccccc; font-family: Arial, Helvetica, Sans-Serif; Color: #000088; }\
    </style>\
  </head>\
  <body>\
    <h1>Connected!</h1>\
  </body>\
</html>");
  server.send ( 200, "text/html", temp );

}

void handleNotFound() {
  String message = "File Not Found\n\n";
  message += "URI: ";
  message += server.uri();
  message += "\nMethod: ";
  message += ( server.method() == HTTP_GET ) ? "GET" : "POST";
  message += "\nArguments: ";
  message += server.args();
  message += "\n";

  for ( uint8_t i = 0; i < server.args(); i++ ) {
    message += " " + server.argName ( i ) + ": " + server.arg ( i ) + "\n";
  }

  server.send ( 404, "text/plain", message );
}

void temper()
{
  server.send (404, "text/plain",celsiy);
  
  HTTPClient http;
  
  http.begin("http://192.168.43.119:8000/api/set");
  int httpCode = http.GET();
  if(httpCode == HTTP_CODE_OK)
  {
      Serial.print("HTTP response code ");
      Serial.println(httpCode);
      String response = http.getString();
      Serial.println(response);
  }
  else
  {
    Serial.println("Error in HTTP request");
  }
  
  http.end();
  Serial.println();
}

void temper1()
{
 double Temp;
 Temp = log(((10240000/analogRead(A0)) - 10000));
  Temp = 1 / (0.001129148 + (0.000234125 + (0.0000000876741 * Temp * Temp ))* Temp );
  Temp = Temp - 273.15; 
  Serial.println(Temp);
 //server.send ( 200, "text/plain", reading );
} 

void lighton()
{
  server.send (404, "text/plain","light on");
  digitalWrite(5,HIGH);
}

void lightoff()
{
  server.send (404, "text/plain","light off");
  digitalWrite(5,LOW);
}

void setup ( void ) {
  Serial.begin ( 9600 );
  WiFi.begin ( ssid, password );
  Serial.println ( "" );
  pinMode(5,OUTPUT);
  // Wait for connection
  while ( WiFi.status() != WL_CONNECTED ) {
    delay ( 500 );
    Serial.print ( "." );
  }

  Serial.println ( "" );
  Serial.print ( "Connected to " );
  Serial.println ( ssid );
  Serial.print ( "IP address: " );
  Serial.println ( WiFi.localIP() );

  if ( MDNS.begin ( "esp8266" ) ) {
    Serial.println ( "MDNS responder started" );
  }

  server.on ( "/", handleRoot );
  server.on ( "/temperature", temper );
  server.on ( "/set", temper1 );
  server.on ( "/lighton", lighton );
  server.on ( "/lightoff", lightoff );
  server.on ( "/inline", []() {
    server.send ( 200, "text/plain", "this works as well" );
  } );
  server.onNotFound ( handleNotFound );
  server.begin();
  Serial.println ( "HTTP server started" );
}

void loop ( void ) {
  server.handleClient();
}
