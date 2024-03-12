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
import sys


class HBNBCommand(cmd.Cmd):
    """
    Command-line interpreter for the HBNB project.

    Attributes:
        prompt (str): The prompt to be displayed on the command line.
        supported_classes (dict): A dictionary mapping supported class
        names to their corresponding classes.
    """
    prompt = "(hbnb) "

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def do_EOF(self, line):
        '''exits the cmd loop'''
        return True

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
        if args[0] in HBNBCommand.supported_classes:
            obj = HBNBCommand.supported_classes[args[0]]()
            obj.save()
            print(obj.id)
            return
        else:
            print(f"** class doesn't exist **")
            return

    def help_create(self):
        """Create Help Method"""
        print(f"Create a new instance of a supported class.\n"
              "\nUsage: create <class name>\n"
              "\nExample:"
              "\ncreate BaseModel")

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
        if args[0] in HBNBCommand.supported_classes:
            instance_id = args[1]
            instance_key = f"BaseModel.{instance_id}"
            # Retrieving all instances from the storage.
            objs = storage.all()
            if instance_key in objs:
                instance = (HBNBCommand.supported_classes[args[0]]
                            (**objs[instance_key]))
                print(instance)
                return
            else:
                print(f"** no instance found **")
                return

    def help_show(self):
        """help method of Show"""
        print(f"Display details of a specific instance.\n"
              "\nUsage: show <class name> <instance id>\n"
              "\nExample:"
              "\nshow BaseModel 1234-5678-9012")

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
        if args[0] in HBNBCommand.supported_classes:
            instance_id = args[1]
            instance_key = f"BaseModel.{instance_key}"
            objs = storage.all()
            if instance_key in objs:
                del objs[instance_key]
                storage.save()
            else:
                print(f"** no instance found **")
                return
        else:
            print(f"** class doesn't exist **")
            return

    def help_destroy(self):
        """Help Method of Destroy"""
        print(f"Delete an instance based on the class name and instance id.\n"
              "\nUsage: destroy <class name> <instance id>"
              "\nExample:"
              "\ndestroy BaseModel 1234-5678-9012")

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

    def help_all(self):
        """Help method of all)"""
        print(f"Display all instances or instances of a specified class.\n"
              "\nUsage: all [<class name>]\n"
              "\nIf no class name is provided, all instances "
              "will be displayed\n"
              "\nExample:"
              "\nall"
              "\nall BaseModel")

    def do_update(self, line):
        """
        Update attributes of an instance.

        Args:
            line (str): The input command line containing class name,
            instance id, attribute name, and new value.

        Returns:
            None
        """
        if not line:
            print("** class name missing **")
            return

        args = shlex.split(line)
        if len(args) < 2:
            if args[0] in HBNBCommand.supported_classes:
                print("** instance id missing **")
                return
            else:
                print("** class doesn't exist **")
            return

        class_name = args[0]
        instance_id = args[1]
        instance_key = f"BaseModel.{instance_id}"
        objs = storage.all()

        if class_name not in HBNBCommand.supported_classes:
            print("** class doesn't exist **")
            return

        if instance_key not in objs:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        new_value = args[3]

        # Update the attribute value
        obj = objs[instance_key]
        obj[attribute_name] = eval(new_value)
        storage.save()

    def do_update(self):
        """Help method for update"""
        print(f"Update attributes of an instance.\n"
              "\nUsage: update <class name> <instance id> <attribute name>"
              "<new value>\n"
              "\nExample:"
              "\nupdate BaseModel 1234-5678-9012 name 'New Name'")

    def do_EOF(self, line):
        """
        Exit the command-line interpreter when encountering EOF (Ctrl+D).

        Args:
            line (str): Unused. Represents the input command line.

        Returns:
            bool: True to exit the interpreter.
        """
        return True

    def help_EOF(self):
        """help method for EOF"""
        print(f"Exit the command-line interpreter when encountering"
              " EOF (Ctrl+D).\n"
              "\nUsage: Press Ctrl+D\n"
              "\nExample:"
              "\nPress Ctrl+D to exit")

    def do_quit(self, line):
        """
        Exit the command-line interpreter.

        Args:
            line (str): Unused. Represents the input command line.

        Returns:
            bool: True to exit the interpreter.
        """
        return True

    def help_quit(self):
        """help method for quit"""
        print(f"Exit the command-line interpreter.\n"
              "\nUsage: quit\n"
              "\nExample:"
              "\nquit")

    def emptyline(self):
        """
        When an empty line + ENTER shouldn’t
        execute anything
        """
        pass


if __name__ == '__main__':
    if len(sys.argv) == 1:
        HBNBCommand().cmdloop()
    else:
        HBNBCommand().onecmd(' '.join(sys.argv[1:]))
