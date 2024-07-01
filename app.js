import logger from './logger.js';

// Simulate some application logic and logging
function startApplication() {
    logger.info('Cake Paradise application started');
    
    try {
        // Simulate an operation that could fail
        performCriticalOperation();
    } catch (error) {
        logger.error(`Critical operation failed: ${error.message}`);
    }
    
    logger.info('Application is running smoothly');
}

function performCriticalOperation() {
    // Simulating an error
    throw new Error('Simulated error');
}

// Start the application
startApplication();

