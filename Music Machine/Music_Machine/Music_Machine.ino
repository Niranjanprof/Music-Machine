// Niranjan prof
//https://github.com/Niranjanprof
//Mailme @ niranjannb7777@gmail.com

// Music Machine Project


# define trig1 2
# define echo1 3
# define trig2 4
# define echo2 5
# define trig3 6
# define echo3 7
# define trig4 8
# define echo4 9

void setup() {
  pinMode(trig1,OUTPUT);
  pinMode(echo1,INPUT);
  pinMode(trig2,OUTPUT);
  pinMode(echo2,INPUT);            //Four Ultra Sonic Sensors
  pinMode(trig3,OUTPUT);
  pinMode(echo3,INPUT);
  pinMode(trig4,OUTPUT);
  pinMode(echo4,INPUT);
  Serial.begin(9600);             //Serial Monitor
}

void loop() {

  digitalWrite(trig1,LOW);
  delay(2);
  digitalWrite(trig1,HIGH);
  delay(10);
  digitalWrite(trig1,LOW);        // Sensor 1 :-  Controller 1
  int a= pulseIn(echo1,HIGH);
  a/=100;
  String str1=String(a);


  digitalWrite(trig2,LOW);
  delay(2);
  digitalWrite(trig2,HIGH);
  delay(10);
  digitalWrite(trig2,LOW);        // Sensor 2 :-  Controller 2
  int b= pulseIn(echo2,HIGH);
  b/=100;
  String str2=String(b);

  digitalWrite(trig3,LOW);
  delay(2);
  digitalWrite(trig3,HIGH);
  delay(10);
  digitalWrite(trig3,LOW);        // Sensor 3 :-  BGM Controller 
  int a= pulseIn(echo3,HIGH);
  c/=100;
  String str3=String(a);
  
  
  digitalWrite(trig3,LOW);
  delay(2);
  digitalWrite(trig3,HIGH);
  delay(10);
  digitalWrite(trig3,LOW);        // Sensor 4 :- Delay Sensor
  int d= pulseIn(echo3,HIGH);
  d/=100;
  if(d>22)                         //Stoping it form infinite delay
    d=20
  

  String str=str1+"+"+str2+"-"+str3; //Sending to Monitor as single string
  Serial.println(str);
  delay(d*100);                      // Delay (Tempo) Between Notes Can be also applied in python using time.sleep(seconds)
}
