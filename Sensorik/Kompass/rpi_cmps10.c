//CMPS10 example c code for RaspberryPi

#include <stdio.h>
#include <stdlib.h>
#include <linux/i2c-dev.h>
#include <fcntl.h>
#include <string.h>
#include <sys/ioctl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>

int fd;
char *fileName = "/dev/i2c-1";
int address = 0x60;
unsigned char buf[5];

signed int getBearingAsByte(){
	return buf[1];
}

float getBearingAsDecimal() {
	unsigned char highByte = buf[2];
	unsigned char lowByte = buf[3];
	unsigned int result = (highByte <<8) + lowByte;
	float resultChar = (result / 10) + (result % 10);

	return resultChar;
}

signed int getPitch() {
	signed int result;
		
	if  (buf[4] > 128) {
		buf[4] = 0 - buf[4];
		result = buf[4] * -1;
        } else {
		result = buf[4];
	}
	
	return result;
}

signed int getRoll() {
	signed int result;

	if  (buf[5] > 128) {
		buf[5] = 0 - buf[5];
		result = buf[5] * -1;
	} else {
		result = buf[5];
	}

	return result;
}

int main(int argc, char **argv)
{
	printf("*** CMPS10 example ***\n");

	//int fd;
	//char *fileName = "/dev/i2c-1";
	//int address = 0x60;
	//unsigned char buf[5];

	if ((fd = open(fileName, O_RDWR)) < 0) {
		printf("Failed to open i2c port \n");
		exit(1);
	}

	if (ioctl(fd, I2C_SLAVE, address) < 0) {
		printf("Unable to get bus access to talk to slave\n");
		exit(1);
	}

	buf[0] = 0;

	if ((write(fd, buf, 1)) != 1) {
		printf("Error writing to i2c slave\n");
		exit(1);
	}

	if (read(fd, buf, 6) != 6) {
		printf("Unable to read from slave\n");
	} else {
		printf("Software v: %u \n", buf[0]);
		printf("Bearing as byte: %u \n", buf[1]);

//		unsigned char highByte = buf[2];
//		unsigned char lowByte = buf[3];
//		unsigned int result = (highByte <<8) + lowByte;
//		printf("Bearing as decimal: %u.%u\n", result / 10, result %10);

		printf("Pitch: %i\n", getPitch());
		printf("Roll: %i\n", getRoll());
		printf("Bearing as decimal %.3f\n", getBearingAsDecimal());
	}

	return 0;
}
