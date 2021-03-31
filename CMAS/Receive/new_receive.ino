#include <RH_ASK.h>
// Include dependant SPI Library 
#include <SPI.h> 
 

RH_ASK radio;
 
void setup()
{
    // Initialize ASK Object
    radio.init();
    // Setup Serial Monitor
    Serial.begin(9600);
}
 
void loop()
{
    uint8_t buf[24];
    uint8_t buflen = sizeof(buf);
    delay(1000);
 
    if (radio.recv(buf, &buflen))
    {
      
      Serial.print("Id Received: PersonX");
      Serial.println((char*)buf);         
    }
    else{
      Serial.println("Id Received: PersonX");
    }
}
