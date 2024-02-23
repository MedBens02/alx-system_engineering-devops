#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

/**
 * infinite_while - Goes to an infinite loop
 *
 * Return: Always 0 (Success)
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Creates zombie children processes
 *
 * Return: Always 0 (Success)
 */
int main()
{
	pid_t pid;
	int i = 0;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid <= 0)
			exit(0);
		else
		{
			printf("Zombie process created, PID: %d\n", pid);
			sleep(1);
		}
	}
	infinite_while();

	return (0);
}
