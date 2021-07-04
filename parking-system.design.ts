/**
 * Basic driver entity that would encapsulate
 * driver related information.
 */
export class Driver {
    constructor(
        readonly numberPlate: string, 
        readonly driverAge: number
    ) {}
}

/**
 * Slot entity that would encapsulate
 * slot's imformation and state
 */
export class Slot {

    /**
     * Provides information based on whether
     * the given slot is open or closed
     * Default OPEN
     */
    private state: 'OPEN' | 'CLOSED' = 'OPEN';

    /**
     * Driver reference
     * Default null
     */
    private driver: Driver = null;

    constructor(readonly slotNo: number) {}

    public isSlotAssignable(): boolean {
        return this.state === 'OPEN' && !this.driver;
    }

    public getAssignedDriver(): Driver {
        return this.driver;
    }

    public addDriver(driver: Driver): void {
        if (!driver || this.state === 'CLOSED') {
            throw new Error('Unable to add driver');
        }
        this.driver = driver;
    }

    public removeDriver(): void {
        this.driver = null;
        this.state = 'OPEN';
    }
}

export class ParkingLotSystem {

    /**
     * Using hashmap to store the slots,
     * Ideally should be using database for managing
     * real world cases
     */
    private slots: Map<number, Slot> = new Map<number, Slot>();

    constructor(readonly numOfSlots: number = 1000) {
        this.initSlots(numOfSlots);
    }

    /**
     * Initiates the parking slots
     * @param numOfSlots Number of initial parking slots available
     */
    private initSlots(numOfSlots: number) {
        if (numOfSlots && numOfSlots <= 0) {
            throw new Error('Invalid initial number of slots provided');
        }
        for (let i=0; i<numOfSlots; i++) {
            // i is used here as slot number
            this.slots.set(i, new Slot(i));
        }
    }

    /**
     * Assigns a slot number to the driver
     * @param driver driver reference
     */
    public assignSlotNumber(driver: Driver): number {
        if (!driver) {
            throw new Error('Not a valid driver reference');
        }
        const slot: Slot = this.getValidSlot();
        if (!slot) {
            throw new Error('All slots are assigned. Please try again later');
        }
        slot.addDriver(driver);
        return slot.slotNo;
    }

    public freeSlotByNumber(slotNo: number): void {
        if (!slotNo || !this.slots.has(slotNo)) {
            throw new Error('Not a valid slot number');
        }
        const slot: Slot = this.slots.get(slotNo);
        slot.removeDriver();
    }

    /**
     * Provides a valid slot instance. returns null if no such slot is found
     * @param driver Optional driver reference. Since we are not taking in account
     * how driver information is important in order to calc valid slot, it is passed
     * as optional criterion
     */
    private getValidSlot(driver?: Driver): Slot {
        let assignableSlot: Slot = null;

        /**
         * We can add more constraints here as to how
         * we would want to select assignable slots
         */
        this.slots.forEach((slot: Slot) => {
            if (slot.isSlotAssignable()) {
                assignableSlot = slot; 
            }
        });
        return assignableSlot;
    }
}