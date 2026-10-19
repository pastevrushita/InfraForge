
output "vpc_id" {
  description = "ID of the InfraForge VPC"
  value       = aws_vpc.main.id
}

output "public_subnet_id" {
  description = "ID of the public subnet"
  value       = aws_subnet.public.id
}

output "private_subnet_id" {
  description = "ID of the private subnet"
  value       = aws_subnet.private.id
}

output "web_security_group_id" {
  description = "ID of the web security group"
  value       = aws_security_group.web.id
}

output "ec2_public_ip" {
  description = "Public IPv4 address of the InfraForge web server"
  value       = aws_instance.web.public_ip
}
