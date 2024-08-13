#include <Wire.h>
#include <MPU6050.h>

#define CONVERT_G_TO_MS2    9.80665f

MPU6050 mpu;

void setup() {
  Serial.begin(9600);
  Wire.begin();
  mpu.initialize();
} 
 

void loop() {
  // Ler os dado de acelerômetro e giroscípio
  int16_t ax, ay, az, gx, gy, gz;
  mpu.getMotion6(&ax, &ay, &az, &gx, &gy, &gz);
  
  // Converter valores brutos em unidades significativas
  float accelX_g = ax / 16384.0; // multiplo de g
  float accelY_g = ay / 16384.0; // multiplo de g
  float accelZ_g = az / 16384.0; // multiplo de g
  float accelX = accelX_g * CONVERT_G_TO_MS2; // m/s²
  float accelY = accelY_g * CONVERT_G_TO_MS2; // m/s²
  float accelZ = accelZ_g * CONVERT_G_TO_MS2; // m/s²
  float gyroX = gx / 131.0;   // (graus/s)
  float gyroY = gy / 131.0;   // (graus/s)
  float gyroZ = gz / 131.0;   // (graus/s)

   
  // Imprimir os valores
  Serial.print("Acelerômetro (g): ");
  Serial.print(accelX);
  Serial.print(", ");
  Serial.print(accelY);
  Serial.print(", ");
  Serial.println(accelZ);
  
  Serial.print("Giroscópio (graus/s): ");
  Serial.print(gyroX);
  Serial.print(", ");
  Serial.print(gyroY);
  Serial.print(", ");
  Serial.println(gyroZ);
  
  Serial.println("-------------------");
  
  delay(1000); // atraso em 1 segundo
}
