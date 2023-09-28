const axios = require('axios');
const { JSDOM } = require('jsdom');

const scriptUrl = 'https://checkout.cloudpayments.ru/checkout.js';

// Create a virtual DOM environment
const dom = new JSDOM(`<!DOCTYPE html><html><head></head><body></body></html>`, {
    runScripts: 'dangerously',
    resources: 'usable',
});

// Set up a simulated window object
const simulatedWindow = dom.window;
global.window = simulatedWindow;

axios.get(scriptUrl)
    .then(async (response) => {
        const scriptContent = response.data;

        // Execute the script in the virtual DOM environment
        simulatedWindow.eval(scriptContent);

        // Your code to create the payment cryptogram can go here
        const fieldValues = {
            cvv: '111',
            cardNumber: '4000 0000 0000',
            expDateMonth: '08',
            expDateYear: '20',
        };

        const checkout = new simulatedWindow.cp.Checkout({
            publicId: 'pk_6b095c74fa619e6d79ddee063375d',
        });
        try {
            const cryptogram = await checkout.createPaymentCryptogram(fieldValues);
            console.log(cryptogram);
        } catch (error) {
            console.log('error')
        }


        // Close the virtual DOM environment
        dom.window.close();
    })
    .catch((error) => {
        console.error('Error loading external script:', error);
    });

// Remove the global window object after executing
delete global.window;
