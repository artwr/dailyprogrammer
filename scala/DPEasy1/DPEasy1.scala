import scala.io.StdIn.readLine

object DPEasy1 {
  def main(args: Array[String]) {
    val name = scala.io.StdIn.readLine("What is your name?\n")
    val age = scala.io.StdIn.readLine("What is your age?\n")
    val username = scala.io.StdIn.readLine("What is your reddit username?\n")

    println(s"your name is ${name}, you are ${age} years old, and your username is ${username}")
 }
}
