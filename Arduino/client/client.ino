#include "esp_http_client.h"
#include <string.h>
#define DATA_MAX_SIZE 512


esp_err_t err;
const esp_http_client_config_t config = {
  .url = "http://192.168.0.100/"
};
esp_http_client_handle_t connHandle;


char *data;
int dataLen;

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

void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200); // set serial for usb printing
  data = malloc(sizeof(char)*DATA_MAX_SIZE);
  dataLen = 0;
  
  initHTTPConnection();
  
}

#define PIN_PHOTORESISTOR A0
int photoresistor = 0;

void readPhotoresistor() {
  photoresistor = analogRead(PIN_PHOTORESISTOR);
  Serial.printf("Photoresistor: %d\n", photoresistor);
  return;
}

void loop() {
  // put your main code here, to run repeatedly:
  readPhotoresistor();
  
  delay(1000);
  
  delay(1000);
}
