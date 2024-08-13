#include <Wire.h>
#include <MPU6050.h>

#define CONVERT_G_TO_MS2    9.80665f
#define FREQUENCY_HZ        62.5
#define INTERVAL_MS         (1000 / (FREQUENCY_HZ + 1))

static unsigned long last_interval_ms = 0;

MPU6050 mpu;

void setup() {
  Serial.begin(115200);
  Wire.begin();
  mpu.initialize();
} 
 

void loop() {
  // Ler os dado de acelerômetro e giroscípio
  int16_t ax, ay, az, gx, gy, gz;

  if (millis() > last_interval_ms + INTERVAL_MS) {
    last_interval_ms = millis();
      mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
      
      // Converter valores brutos em unidades significativas
      float accelX_g = ax / 16384.0; // multiplo de g
      float accelY_g = ay / 16384.0; // multiplo de g
      float accelZ_g = az / 16384.0; // multiplo de g
      float accelX = accelX_g * CONVERT_G_TO_MS2; // m/s²
      float accelY = accelY_g * CONVERT_G_TO_MS2; // m/s²
      float accelZ = accelZ_g * CONVERT_G_TO_MS2; // m/s²
       
      // Imprimir os valores
       Serial.print(accelX);
      Serial.print(", ");
      Serial.print(accelY);
      Serial.print(", ");
      Serial.println(accelZ);  
  }
}
