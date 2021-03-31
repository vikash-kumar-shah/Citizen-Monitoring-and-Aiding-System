#include <RH_ASK.h>
#include <SPI.h>
 
RH_ASK radio(2000, 11, 12);
 
void setup()
{
    Serial.begin(9600); 
 

    if (!radio.init())
    {
         Serial.println("Radio module failed to initialize");
    }
}
 
void loop()
{

    const char *msg = "PersonX";
 
    radio.send((uint8_t*)msg, strlen(msg));
 
    radio.waitPacketSent();
 
    delay(1000);
 
    Serial.println(msg);
}
