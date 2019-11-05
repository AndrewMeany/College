.globl	main

.data
	str2Int:	.word
	inputStr:	.space 2
	userInput: 	.asciiz "Enter a two-digit integer [00-99]: "
	userReturn: 	.asciiz "\nYou entered: "
	error:		.asciiz "Please use integer values only"

.text

	main:
	
		### INPUT MESSAGE ###
		la $a0, userInput		# load userInput message into $a0
		li $v0, 4			# set $v0 to 4 for printing a string
		syscall				# print userInput message
		
		### RECEIVE INPUT ###
		li $v0, 8			# load read_string (8) into $v0
		la $a0, inputStr		# allocate string space to $a0
		li $a1, 3			# allocate 2 bytes for string (n-1)
		move $t0, $a0			# set $a0 (string) t0 $t0
		syscall				# perform syscall	
	
		### CONVERT TO INTEGER ###
		lbu $t1, 0($t0)			# select the first digit (10s) in #t1 using least significatn bit unsigned
		blt $t1, 48, stop		# if $t1 < 0 branch to 'stop'
		sub $t1, $t1, 48		# subtract 48 from the ascii
		mul $t1, $t1, 10		# mulitply by 10 to get the int
		
		lbu $t2, 1($t0)			# select the second digit (1s) in #t2 using least significatn bit unsigned
		bgt $10, 57, stop		# if $t2 > 57 branch to 'stop'
		sub $t2, $t2, 48		# subtract 48 from the ascii
		add $t0, $t1, $t2		# add both values in $t1 and $t2 and palce them in $t0
		
		sw $t0, str2Int			# store the value in $t0 in the variable str2Int
			
		### OUTPUT MESSAGE ###
		la $a0, userReturn		# load userReturn message into $a0
		li $v0, 4			# set v0 to 4
		syscall				# print userInput message
		
		add $a0, $zero, $t0		# add $t0 to $a0 for printing
		li $v0, 1			# set $v0 to 1 for printing an integer
		syscall				# perform syscall
		
		### CONVERT TO BINARY ###
		
		
		j exit				# program has run effectively and can now branch to exit
		
	stop:
		### STOP PROGRAM & RESTART ###
		li $v0, 4			
		la $a0, error
		b main
	
	exit:
		### EXIT PROGRAM ###
		li $v0, 10
		syscall
