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
            return

        args = shlex.split(line)
        if len(args) == 1:
            if args[0] in HBNBCommand.supported_classes:
                obj = HBNBCommand.supported_classes[args[0]]()
                obj.save()
                print(obj.id)
                return
            else:
                print(f"** class doesn't exist **")
                return
        else:
            print(f"Usage: Create <class name>")

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
                instance_id = f"BaseModel.{args[1]}"
                # Retrieving all instances from the storage.
                objs = storage.all()
                if instance_id in objs:
                    instance = (HBNBCommand.supported_classes[args[0]]
                                (**objs[instance_id]))
                    print(instance)
                    return
                else:
                    print(f"** no instance found **")
                    return
        else:
            print("Usage: Show <class name> <instance id>")
            return

    def do_destroy(self, line):
        """
        Delete an instance based on the class name and instance id.

        Args:
            line (str): The input command line containing class name and
            instance id.

        Returns:
            None
        """
        if not line:
            print(f"** class name missing **")
            return
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
                instance_id = f"BaseModel.{args[1]}"
                objs = storage.all()
                if instance_id in objs:
                    del objs[instance_id]
                    storage.save()
                else:
                    print(f"** no instance found **")
                    return
            else:
                print(f"** class doesn't exist **")
                return
        else:
            print(f"Usage: destroy <class name> <instance id>")

    def do_all(self, line):
        """
        Display details of all instances or instances of a specific class.

        Args:
            line (str): The input command line containing optional
            class name.

        Returns:
            None
        """
        objs = storage.all()
        instances = []
        if not line:
            for key, value in objs.items():
                instance = (HBNBCommand.supported_classes[objs[key]
                            ['__class__']](**value))
                instances.append(instance.__str__())
            print(instances)
            return
        args = shlex.split(line)
        if len(args) == 1:
            if args[0] in HBNBCommand.supported_classes:
                for key, value in objs.items():
                    if value['__class__'] == args[0]:
                        instance = (HBNBCommand.supported_classes[objs[key]
                                    ['__class__']](**value))
                        instances.append(instance)
                print(instances)
                return
            else:
                print(f"** class doesn't exist **")
                return
        else:
            print(f"Usage: all (class name)")

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
