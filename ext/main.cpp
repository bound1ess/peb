#include <phpcpp.h>

// @TODO add anything you want

/**
 *  Tell the compiler that the get_module is a pure C function.
 */
extern "C" 
{    
    /**
     *  Function that is called by PHP right after the PHP process
     *  has started, and that returns an address of an internal PHP
     *  strucure with all the details and features of your extension.
     *
     *  @return void* a pointer to an address that is understood by PHP
     */
    PHPCPP_EXPORT void *get_module() 
    {
        /**
		 *  Static(!) Php::Extension object that should stay in memory
         *  for the entire duration of the process (that's why it's static).
		 */
        static Php::Extension extension("yourextension", "0.0.0");
        
        // @TODO add your own functions, classes, namespaces to the extension
        
        return extension;
    }
}
