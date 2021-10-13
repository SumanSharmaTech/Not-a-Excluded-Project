public class String_Methods {
  public static void main(String[] args) {

    String s = "  My name is Ramyak Rohan Mohanty  ";

    System.out.println("\nOriginal string is: " + s);

    int strlen = s.length();

    System.out.println("\nLength of the string is: " + strlen);

    String s_UpperCase = s.toUpperCase();

    System.out.println("\nString in uppercase is: " + s_UpperCase);

    String s_LowerCase = s.toLowerCase();

    System.out.println("\nString in lowercase is: " + s_LowerCase);

    String s_ReplacedString = s.replace("Rohan", "Kumar");

    System.out.println("\nString with \'Rohan\' replaced with \'Kumar\' is: " + s_ReplacedString);

    String s_TrimmedString = s.trim();
    
    System.out.println("\nString with whitespaces trimmed is: " + s_TrimmedString);

    String s_SubString1 = s.substring(5);
    
    System.out.println("\nString with substring extracted from 5th index to the end is: " + s_SubString1);

    String s_SubString2 = s.substring(13, 33);
    
    System.out.println("\nString with substring extracted from 13th index to the 33rd index is: " + s_SubString2);

    char s_ExtractedCharacter = s.charAt(6);

    System.out.println("\nCharacter extracted at 6th index from the string is: " + s_ExtractedCharacter);

    boolean doesTheStringStartWithA = s_TrimmedString.startsWith("A");
    
    System.out.println("\nThe string does not start with the letter \'A\' since the value is " + doesTheStringStartWithA);

    boolean doesTheStringEndWithY = s_TrimmedString.endsWith("y");

    System.out.println("\nThe string does end with the letter \'Y\' since the value is " + doesTheStringEndWithY);

    boolean doesTheStringEquateToMyNameIsRamyakRohanMohanty = s_TrimmedString.equals("my name is ramyak rohan mohanty");

    System.out.println("\nThe string does not equate to the given string since the value is " + doesTheStringEquateToMyNameIsRamyakRohanMohanty);

    boolean doesTheStringEquateToMyNameIsRamyakRohanMohantyIgnoringCase = s_TrimmedString.equalsIgnoreCase("my name is ramyak rohan mohanty");

    System.out.println("\nThe string equates to the given string while ignoring case-sensitivity since the value is " + doesTheStringEquateToMyNameIsRamyakRohanMohantyIgnoringCase);

  }
}