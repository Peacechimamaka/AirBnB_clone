#!/usr/bin/python3
"""
    This interpreter provides a command-line interface for interacting with
    the HBNB project(AirBnB clone). It supports commands for creating and
    manipulating instances of supported classes.
"""
import cmd
from models.base_model import BaseModel
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):
    """
        Command-line interpreter for the HBNB project.

        Attributes:
            prompt (str): The prompt to be displayed on the command line.
            supported_classes (dict): A dictionary mapping supported class
            names to their corresponding classes.
    """
    prompt = "(hbnb) "

    # Mapping of supported class names to their corresponding class objects.
    supported_classes = {
            'BaseModel': BaseModel
    }

    def do_create(self, line):
        """
            Create a new instance of a specified class.

            Args:
                line (str): The input command line containing the class name.

            Returns:
                None
        """
        if not line:
            print(f"** class name missing **")
        else:
            if line in HBNBCommand.supported_classes:
                obj = HBNBCommand.supported_classes[line]()
                obj.save()
                print(obj.id)
            else:
                print(f"** class doesn't exist **")

    def do_show(self, line):
        """
            Display details of a specific instance.

            Args:
                line (str): The input command line containing the class name
                and instance ID.

            Returns:
                None
        """
        if not line:
            print(f"** class name missing **")
            return
        # Splitting the command line arguments.
        args = shlex.split(line)
        if len(args) == 1:
            if args[0] in HBNBCommand.supported_classes:
                print(f"** instance id missing **")
                return
            else:
                print(f"** class doesn't exist **")
                return
        if len(args) == 2:
            if args[0] in HBNBCommand.supported_classes:
                class_id = f"BaseModel.{args[1]}"
                # Retrieving all instances from the storage.
                objs = storage.all()
                if class_id in objs:
                    class_instance = (HBNBCommand.supported_classes[args[0]]
                                      (**objs[class_id]))
                    print(class_instance)
                    return
                else:
                    print(f"** no instance found **")
                    return

    def do_EOF(self, line):
        """
            Exit the command-line interpreter when encountering EOF (Ctrl+D).

            Args:
                line (str): Unused. Represents the input command line.

            Returns:
                bool: True to exit the interpreter.
        """
        return True

    def do_quit(self, line):
        """
            Exit the command-line interpreter.

            Args:
                line (str): Unused. Represents the input command line.

            Returns:
                bool: True to exit the interpreter.
        """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
