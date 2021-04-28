#include "esp_http_client.h"
#include "WiFi.h"
#include <string.h>
#define DATA_MAX_SIZE 512

esp_err_t err;
const esp_http_client_config_t config = {
  .url = "http://192.168.0.100:8000/receive_data"
  //.port = 8000, 
};
esp_http_client_handle_t connHandle;


const char* ssid = "tarta2";
const char* password =  "AguaSanJoaquin2litros";


char *data;
int dataLen;

uint8_t dev_id;

void initHTTPConnection() {
  connHandle = esp_http_client_init(&config);
  esp_http_client_set_method(connHandle, HTTP_METHOD_POST);
  
}

/*
 * Make POST request with data on data variable.
 */
void sendPOST() {
  dataLen = strlen(data);
  esp_http_client_set_method(connHandle, HTTP_METHOD_POST);
  esp_http_client_set_post_field(connHandle, data, dataLen);
  err = esp_http_client_perform(connHandle);
  Serial.printf("Request made, err: %d", err);
}


void getDevID() {
  char* toColonPlus;
  int offset = 0;
  esp_http_client_config_t set = {
    .url = "http://192.168.0.100:8000/getid"
    //.port = 8000,
  };

  esp_http_client_handle_t conn = esp_http_client_init(&set);
  esp_http_client_set_method(conn, HTTP_METHOD_GET);
  err = esp_http_client_perform(conn);

  if(err == ESP_OK) {
    dataLen = esp_http_client_read(conn, data, DATA_MAX_SIZE);
    Serial.printf("dataLen = %d, dev_id: %d\n", dataLen, dev_id);

    toColonPlus = strchr(data, ':');
    toColonPlus++;
    while(*(toColonPlus+offset) != '}') {
      offset++;
    }
    *(toColonPlus+offset) = '\0';
    dev_id = atoi(toColonPlus);
  }
  else {
    
dev_idError:
    Serial.println("error in get dev_id");
    delay(10000);
    goto dev_idError;
  }
  
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200); // set serial for usb printing
  data = (char*)malloc(sizeof(char)*DATA_MAX_SIZE);
  dataLen = 0;
 
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.println("Connecting to WiFi..");
  }
 
  Serial.println("Connected to the WiFi network");
  
  getDevID();
  initHTTPConnection();

  
}

#define PIN_PHOTORESISTOR A0
uint16_t photoresistor = 0;

void readPhotoresistor() {
  photoresistor = analogRead(PIN_PHOTORESISTOR);
  Serial.printf("Photoresistor: %d\n", photoresistor);
  return;
}



void prepareData() {
  dataLen=sprintf (data, "%d\nlight,%d", dev_id, photoresistor);
  
}

void sendData() {
  esp_http_client_set_method(connHandle, HTTP_METHOD_POST);
  esp_http_client_set_post_field(connHandle, data, dataLen);
  err = esp_http_client_perform(connHandle);
  
  if(err == ESP_OK) {
   Serial.printf("%s\n----------------", data);
  }
  else {
    
sendDataError:
    Serial.println("error in get sendData");
    delay(10000);
    goto sendDataError;
  }
}

void loop() {
  // put your main code here, to run repeatedly:

  
  readPhotoresistor();
  prepareData();
  sendData();
  
  delay(1000);
  
  delay(1000);
}
