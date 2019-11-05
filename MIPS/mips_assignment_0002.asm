.globl	main

.data 
	str2Int:	.word
	inputStr:	.space 7									# set input variable and assign 7 bytes
	str2float:	.float 1									# set float variable
	
	userInput:	.asciiz 	"Enter a real number [xxx.yyy]: "				# input message
	space: 		.asciiz 	" "								# string for creating a space
	userReturn1: 	.asciiz 	"\nYou entered the integer: "					# output message for integer
	userReturn2:	.asciiz		"\nYou entered the float: "					# output message for float
	userReturn3:	.asciiz		"\nThe sign bit of your number is: "				# output message for sign
	userReturn4:	.asciiz		"\nThe exponent of your number is: "				# output message for exponent
	userReturn5:	.asciiz		"\nThe fraction of your number is: "				# output message for fraction
	errorMessage:	.asciiz		"\nThe input has an invalid character! Please try again.\n"	# output message for error
	
	
	printPeriod:	.byte		'.'					# . output
	floatDiv:	.float 1000						# value for float division
.text

	main:
		### INPUT MESSAGE ###
		li $v0, 4			# set $v0 to 4 for printing a string
		la $a0, userInput		# load userInput message into $a0
		syscall				# perform syscall to print userInput message

		### RECEIVE INPUT ###
		li $v0, 8			# load read_string (8) into $v0
		la $a0, inputStr		# allocate string space to $a0
		li $a1, 8			# allocate 7 bytes for string (n-1)
		move $t0, $a0			# set $a0 (string) t0 $t0
		syscall				# perform syscall for reading input
		
		### CONVERT TO INTEGER ###
		lbu $t1, 0($t0)			# set the first digit (100s) to t1 using least significatn bit unsigned
		blt $t1, 48, error		# if character entered is less than 48 branch to 'error'
		bgt $t1, 57, error		# if character entered is more than 57 branch to 'error'
		addi $t1, $t1, -48		# subtract 48 from the ascii to get the decimal value
		mul $t1, $t1, 100		# mulitply by 100 to set the first digit
		
		lbu $t2, 1($t0)			# set the second digit (10s) to $t2 using least significatn bit unsigned
		blt $t2, 48, error		# if character entered is less than 48 branch to 'error'
		bgt $t2, 57, error		# if character entered is more than 57 branch to 'error'
		addi $t2, $t2, -48		# subtract 48 from the ascii to get the decimal value
		mul $t2, $t2, 10		# mulitply by 10 to set the second digit
		add $t4, $t1, $t2		# add values in $t1 (100s) and $t2 (10s) and place them in $t4
		
		lbu $t3, 2($t0)			# set the third digit (1s) to $t3 using least significatn bit unsigned
		blt $t3, 48, error		# if character entered is less than 48 branch to 'error'
		bgt $t3, 57, error		# if character entered is more than 57 branch to 'error'
		addi $t3, $t3, -48		# subtract 48 from the ascii to get the decimal value
		add $t5, $t4, $t3		# add both values in $t4 (100s + 10s) and $t3 (1s) and place them in $t5
		
		lbu $t1, 4($t0)			# set the fourth digit (.1s) to $t1 using least significatn bit unsigned
		blt $t1, 48, error		# if character entered is less than 48 branch to 'error'
		bgt $t1, 57, error		# if character entered is more than 57 branch to 'error'
		addi $t1, $t1, -48		# subtract 48 from the ascii to get the decimal value
		mul $t1, $t1, 100		# mulitply by 100 to set the fourth digit
		
		lbu $t2, 5($t0)			# set the fifth digit (.01s) to $t2 using least significatn bit unsigned
		blt $t2, 48, error		# if character entered is less than 48 branch to 'error'
		bgt $t2, 57, error		# if character entered is more than 57 branch to 'error'
		addi $t2, $t2, -48		# subtract 48 from the ascii to get the decimal value
		mul $t2, $t2, 10		# mulitply by 10 to set the fifth digit
		add $t4, $t1, $t2		# add values in $t1 (.1s) and $t2 (.01s) and place them in $t4
		
		lbu $t3, 6($t0)			# set the sixth digit (.001s) to $t3 using least significatn bit unsigned
		blt $t3, 48, error		# if character entered is less than 48 branch to 'error'
		bgt $t3, 57, error		# if character entered is more than 57 branch to 'error'
		addi $t3, $t3, -48		# subtract 48 from the ascii to get the decimal value
		add $t6, $t4, $t3		# add both values in $t4 (.1s + .01s) and $t3 (.001s) and place them in $t6
		
		### CONVERT TO FLOAT ###
		
		mtc1 $t5, $f1			# move the value in $t5 to coprocessor1 register $f1 
		cvt.s.w $f1, $f1		# convert the value in $f1 to a float
		
		mtc1 $t6, $f2			# move the value in $t6 to coprocessor1 register $f2 
		cvt.s.w $f2, $f2		# convert the value in $f2 to a float
		
		lwc1 $f3, floatDiv		# load the value (1000) stored in the variable to coprocessor1 register $f3
		
		div.s $f4, $f2, $f3		# divide $f2 by $f3 (1000) to place it behind the decimal in $f4
		
		add.s $f5, $f1, $f4		# add both halves of the value togther and store in $f5
		
		swc1 $f5, str2float		# store the value in $f5 in the variable str2float
				
		#sw $t5, str2Int		# store the value in $t5 in the variable str2Int
		
		### OUTPUT MESSAGE ###
		
		li $v0, 4			# set v0 to 4 to print string
		la $a0, userReturn1		# load userReturn1 message into $a0
		syscall				# print userInput1 message
		
		li $v0, 1			# set $v0 to 1 for printing an integer
		add $a0, $zero, $t5		# add $t0 to $zero and set to $a0 for printing
		syscall				# perform syscall

		li $v0, 4			# set v0 to 4 to print string
		la $a0, printPeriod		# load printPeriod message into $a0
		syscall				# perform syscall

		add $a0, $zero, $t6		# add $t0 to $zero and set to $a0 for printing
		li $v0, 1			# set $v0 to 1 for printing an integer
		syscall				# perform syscall

		### FOR TESTING ###
		li $v0, 4			# set v0 to 4 to print string
		la $a0, userReturn2		# load userReturn2 message into $a0
		syscall				# perform syscall to print float message

		li $v0, 2			# set $v0 to 2 to print float
		lwc1 $f12, str2float		# load str2float value into $f12
		syscall				# perform syscall
		
		### CONVERT TO BINARY AND PRINT ###
		mfc1 $t2, $f5			# set $t1 to value in $f5
	
	loopStart:				# start of binary print loop label
 


	loopEnd:				# end of binary print loop label
		
		li $v0, 4			# set v0 to 4 to print string
		la $a0, userReturn3		# load userReturn3 message into $a0
		syscall				# print sign bit message
		
		li $v0, 4			# set v0 to 4 to print string
		la $a0, userReturn4		# load userReturn4 message into $a0
		syscall				# print exponent message
		
		li $v0, 4			# set v0 to 4 to print string
		la $a0, userReturn5		# load userReturn5 message into $a0
		syscall				# print fraction message
		
		j exit				# program has run effectively and can now branch to exit
		
	error:
		### STOP PROGRAM & RESTART ###
		li $v0, 4			# set $v0 to 4 for printing a string
		la $a0, errorMessage		# load error message into $a0
		syscall				# perform syscall to print error message
		
		j main				# jump back to main to restart programme

	exit:
		### EXIT PROGRAM ###
		li $v0, 10			# set $v0 to 10 (exit)
		syscall				# perform syscall to exit the programme
