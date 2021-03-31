#include "TRIGGER_WIFI.h"               
#include "TRIGGER_GOOGLESHEETS.h"      

char column_name_in_sheets[ ][20] = {"value1"};                       
String Sheets_GAS_ID = "your id";                                        
int No_of_Parameters = 1;                                                                

void setup() 
{
  Serial.begin(9600);
  while (!Serial);

  WIFI_Connect("NascentCoders","vikash123");                                                   
  Google_Sheets_Init(column_name_in_sheets, Sheets_GAS_ID, No_of_Parameters );        
}

void loop() 
{
  char a[100]="PersonX";
  Data_to_Sheets(No_of_Parameters,  a);        

  Serial.println();
  delay(5000);                                 
                                          
}
