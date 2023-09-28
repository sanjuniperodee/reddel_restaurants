const axios = require('axios');
const { JSDOM } = require('jsdom');

const cartArgs = {
    cvv: process.argv[2],             // Default CVV value
    cardNumber: process.argv[3],  // Default card number
    expDateMonth: process.argv[4],     // Default expiration month
    expDateYear: process.argv[5],      // Default expiration year
};

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

        simulatedWindow.eval(scriptContent);

        const checkout = new simulatedWindow.cp.Checkout({
            publicId: 'pk_6b095c74fa619e6d79ddee063375d',
        });
        try {
            const cryptogram = await checkout.createPaymentCryptogram(cartArgs);
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
